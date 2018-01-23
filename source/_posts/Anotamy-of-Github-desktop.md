---
title: Anotamy of Github desktop
date: 2017-12-11 15:30:58
tags:
categories:
    - [JavaScript, React]
    - [JavaScript, Node]
---

### The menu event
Unlike the menu triggering mechnism in `electron`, IPC is utilized here to control menu events and states. `menu-event` event decides the event and the name property of the message object decides which function to execute. The message is emitted from the main process to a render process.

### How to add a menu and implement its functionality
First, `app/src/main-process/menu/build-default-menu.ts` add your menu item in the corresponding place. 
- label: the text displayed in the menu bar
- id: need to figure out!!!
- accelerator: bind to a short cut
- click: emit('name_for_menu_event')

```js
function emit(name: MenuEvent): ClickHandler {
    return (menuItem, window) => {
        if (window) {
            window.webContents.send('menu-event', {name})
        } else {
            ipcMain.emit('menu-event', { name })
        }
    }
}
```

Since the name should be type of `MenuEvent`, we have to add the name to `MenuEvent` before we add a new menu event(a new name).

This `event` will be catched in file `app.tsx` under path `app/src/ui` .
```js
ipcRenderer.on('menu-event', 
                (event: Electron.IPCMessageEvent, {name}: {name: MenuEvent}) => {
                    this.onMenuEvent(name)
                }
              )
```
Then the implementation of that function will happen in the `onMenuEvent()` function. Then this event will be passed to `dispather` and `appstore`. Let's have a look at the `_showPopup()` function in the `app-store.ts`.
```js
public async _showPopup(popup: Popup): Promise<void> {
    this._closePopup()
    this._closeFoldout(FoldoutType.AppMenu)

    this.currentPopup = popup
    this.emitUpdate()
}

private emitUpdate() {
    //...
    window.requestAnimationFrame(() => {
        this.emitUpdateNow()
    })
}

private emitUpdateNow() {
    this.emitQueued = false
    const state = this.getState()
    this.emitter.emit('did-update', state)
    updateMenuState(state, this.appMenu)
}

// Here this function will be call at the initialization of `AppStore`, so fn get registered to be executed once `did-update` event triggered.
private onDidUpdate(fn: (state: IAppState) => void): Disposable {
    return this.emitter.on('did-update', fn)
}
```
Let's redirect to `app.tsx` to see which function is registered
```js
export class App extends React.Component<IAppProps, IAppState> {
    //...

    public constructor(props: IAppProps) {
        super(props)
        //....
        this.state = props.appStore.getState()
        props.appStore.onDidUpdate(state => {
            this.setState(state)
        })
    }
}
```
Here we know that only `App.setState(state)` get called. But notice that when a react component's state get changed, this component will be re-rendered, which meaning the appearance will chagne accordingly. 

If that function does not involve popup, then other function will be defined in `app-store.ts` to handle that event. For popup page, in `app.tsx` there is a private function to render the React DOM:
```js
private currentPopupContent(): JSX.Element | null {
    if (this.state.errors.length) {
        return null
    }

    const popup = this.state.currentPopup
    if (!popup) { return null }

    switch (popup.type) {
        // cases...
    }
}
```

### exploring 'Repository setting'

#### Local repository
```js
export class Repository {
    public readonly id: number
    public readonly path: string
    // If there is a github repo, its name will be used; or, directory name will be used here.
    public readonly name: string
    public readonly gitHubRepository: GitHubRepository | null

    public readonly missing: boolean

    public get hash(): string {
        // single quote should be replaced by backtick
        return '${this.id} + 
                ${this.gitHubRepository && this.gitHubRepository.hash} +
                ${this.path} + 
                ${this.missing} +
                ${this.name}'
    }
}
```
#### Github repo
```js
export class GitHubRepository {
    public readonly dbID: number | null
    public readonly name: string
    public readonly owner: Owner
    public readonly private: boolean | null
    public readonly htmlURL: string | null
    public readonly defaultBranch: string | null
    public readonly cloneURL: string | null
    public readonly parent: GitHubRepository | null

    public get hash(): string {
        // almost concatenate all properties together
    }
}

export class Owner {
    public readonly id: number | null
    public readonly login: string
    public readonly endpoint: string
}
```

### Exploring AppStore
AppStore is a combination of many different stores.
```js
class AppStore {
    public constructor(
        gitHubUserStore: GitHubUserStore,
        cloningRepositoriesStore: CloningRepositoriesStore,
        emojiStore: EmojiStore,
        issuesStore: IssuesStore,
        statsStore: StatsStore,
        signInStore: SignInStore,
        accountsStore: AccountsStore,
        repositoriesStore: RepositoriesStore,
        pullRequestStore: PullRequestStore
    ){ }

    // Add a local repository
    public async _addRepositories(path: ReadonlyArray<string>): 
                            Promise<ReadonlyArray<Repository>> {
        const addedRepositories = new Array<Repository>()
        const lfsRepositories = new Array<Repositories>()
        for (const path of paths) {
            const validatedPath = await validatedRepositoryPath(path)
            if (validatedPath) {
                log.info('adding repository to store')
                const addedRepo = await this.repositoriesStore.addRepository(
                    validatedPath)
                const [refreshedRepo, usingLFS] = await Promise.all([
                    this._repositoryWithRefreshedGitHubRepository(addedRepo),
                    this.isUsingLFS(addedRepo),
                ])
                addedRepositories.push(refreshedRepo)
                // LFS: Large file storage
                if (usingLFS) {
                    lfsRepositoreis.push(refreshedRepo)
                }
            } else {
                const error = new Error('not a git repository')
                this.emitError(error)
            }
        }

        if (lfsRepositories.length > 0) {
            this._showPopup({
                type: PopupType.InitializeLFS,
                repositories: lfsRepositories,
            })
        }
        return addedRepositories
    }
}
```

### Create a new repository
```js
// path: `src/ui/add-repository/create-repository.tsx`
private createRepository = async () => {
    const fullPath = await this.resolveRepositoryRoot()

    try {
        await this.ensureDirectory(fullPath)
        this.setState({ isValidPath: true})
    } catch (e) {
        if (e.code === 'EACCES' && e.errno === -13) {
            return this.setState({ isValidPath: false})
        }
        log.error('the provided path is not valid', e)

        return this.props.dispather.postError(e)
    }

    this.setStae({ creating: true })

    try {
        await initGitRepository(fullPath)
    } catch (e) {
        this.setState({ creating: false })
        log.error('unable to initialize this repository', e)

        return this.props.dispatcher.postError(e)
    }
    const repositories = await this.props.dispatcher.addRepositories([fullPath])
    if (repositories.length < 1) { return }

    const repository = repositories[0]
    if (this.state.createWithReadMe) {
        try {
            await writeDefaultReadme(fullPath, this.state.name)
        } catch (e) {
            log.error('unable to write README', e)
            this.props.dispatcher.postError(e)
        }
    }

    const gitIgnore = this.state.gitIgnore
    if (gitIgnore !== NoGitIgnoreValue) {
        try {
            await writeGitIgnore(fullPath, gitIgnore)
        } catch (e) {
            log.error('unable to write .gitignore file', e)
            this.props.dispatcher.postError(e)
        }
    }

    const description = this.state.description
    if (description) {
        try {
            await writeGitDescription(fullPath, description)
        } catch (e) {
            log.error('unable to write .git/description file', e)
            this.props.dispatcher.postError(e)
        }
    }

    const licenseName = this.state.license === NoLicenseValue.name ? null : this.state.license
    const license = (this.state.licenses || []).find(l => l.name === licenseName)
    if (license) {
        try {
            const author = await getAuthorIdentity(repository)
            await writeLicense(fullPath, license, {
                fullname: author ? author.name : '',
                email: author ? author.email : '',
                year: new Date().getFullYear().toString(),
                description: '',
                project: this.state.name,
            })
        } catch(e) {
            log.error('unable to write LICENSE', e)
            this.props.dispatcher.postError(e)
        }
    }

    try {
        const status = await getStatus(repository)
        const wd = status.workingDirectory
        const files = wd.files
        if (files.length > 0) {
            await createCommit(repository, "Initial commit", files)
        }
    }catch (e) {
            log.error('initial commit failed', e)
            this.props.dispatcher.postError(e)
    }

    this.setState({ creating: false })
    this.updateDefaultDirectory()
    this.props.dispatcher.selectRepository(repository)
    this.props.onDismissed()
}
```

### Clone a repo

Cloning a repo involves several procedures: `src/ui/clone-repository/clone-repository.tsx`: clone() --> same class: cloneImpl() --> dipatcher: clone() --> the git clone process will happen in `appStore`, when successed, return back to dispatcher to add this repo(path), and select it as the current repo.

In `src/lib/stores/cloning-repositories-store.ts`

```js
export class CloingRepositoriesStore {

    public async clone(url: string, path: string, options: CloneOptions): Promise<boolean>{
        // CloingRepository is a simple object only store path and url
        const repository = new CloningRepository(path, url)
        this._repositories.push(repository)

        const title = 'Cloning into' + path

        this.stateByID.set(repository.id, {kind: 'clone', title, value: 0})
        this.emitUpdate()

        let success = true
        try {
            await cloneRepo(url, path, options, progress => {
                this.stateByID.set(repository.id, progress)
                this.emitUpdate()
            })
        } catch (e) {
            success = false

            const retryAction: RetryAction = {
                type: RetryAction.clone,
                url,
                path,
                options,
            }
            e = new ErrorWithMetadate(e, { retryAction, repository})

            this.emitError(e)
        }
        this.remove(repository)
        return success
    }
}
```
Let's have a look at `cloneRepo()` in `src/lib/git/clone.ts`

```js
export async function clone(url: string, path: string, options: CloneOptions, progressCallback?: (progress: ICloneProgress) => void): Promise<void> {
    const env = envForAuthentication(options.account)
    const args = [
    ]
}
```

### Procedure of adding repo and creating repo
From `createRepository()` we know that repo creation is done by git command, then just `selectRepository()` which is accomplished by `AppStore` in `app-store.ts`. 

```js
public async _selectRepository(repository: Repository | CloningRepository | null): Promise<Repository | null> {
    const previouslySelectedRepository = this.selectedRepository

    // This will change the `App` component
    this.selectedRepository = repository
    this.emitUpdate()

    this.stopBackgroundFetching()
    this.stopPullRequestUpdate()

    if (!repository) {
        return Promise.resolve(null)
    }

    if (!(repository instanceof Repository)) {
        return Promise.resolve(null)
    }
    // LastSelectedRepositoryIDKey is just a const string
    localStorage.setItem(LastSelectedRepositoryIDKey, repository.id.toString())

    if (repository.missing) {
        this.removeGitStore(repository)
        return Promise.resolve(null)
    }

    const gitHubRepository = repository.gitHubRepository
    if (gitHubRepository) {
        this._updateIssues(gitHubRepository)

        this.pullRequestStore.getPullRequests(gitHubRepository)
            .then(p => this.updateStateWithPullRequests(p, repository, gitHubRepository))
            .catch(e => {
                console.warn('error getting pull requests for this repo', e)
                }) 
    }

    this._refreshPullRequests(repository)
    await this._refreshRepository(repository)

    if (this.selectedRepository !== repository) {
        return null
    }

    this.stopBackgroundFetching()
    this.stopPullRequestUpdater()

    this.startBackgroundFetching(repository, !previouslySelectedRepository)
    this.startPullRequestUpdate(repository)
    this.refreshMentioables(repository)

    this.addUpstreamRemoteIfNeeded(repository)

    return this._repositoryWithRefreshedGithubRepository(repository)
}
```

Then let's look at the process of adding existing local repo in `src/ui/add-repository/add-existing-repository.tsx`.

```js
private addRepository = async () => {
    this.props.onDismissed()

    const resolvedPath = this.resolvePath(this.state.path)
    const repositories = await this.props.dispatcher.addRepositories([resolvedPath])

    if (repositories && repositories.length) {
        const repository = repositories[0]
        this.props.dispatcher.selectRepository(repository)
    }
}
```

In conclusion, when we add a local repository, firstly it will be added to the `repositoriesStore`, then the `App` will select this repository to show.

### communication and update
Update the appearance of a react component could be finished by `setState()` of that component. Communication between Other classes (such as `AppStore`) and react component are a little complex. First, when the main component gets loaded, it registers a function to the class it wants to communicate. If the class emit certain event, the registered function will be called. That function is used to call the component's `setState()`. Thus, when the class emit certain event, the component will reload itself.

### git command
All git operations are implemented in `app/src/lib/git`. 
















