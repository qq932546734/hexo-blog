---
title: Understanding SSH Key
date: 2017-12-27 17:12:33
tags:
categories:
    - [UNIX, Basic]
---

### What's SSH?

### How to login without password?
1. First, make sure you have a ssh key pair in your computer. Conventionally, ssh key pairs are stored in `~/.ssh/` directory. A ssh key pair are composed of a private key and a public key. The public key is the one you need to upload to the server which you want to login. Remember you must keep your private key secrete. If you don't have one, generate one:
    ```
    $ ssh-keygen 
    ```
    Then you will be promoted to choose a folder to store the key pair and a passphrase, which will be empty if you just press enter(I suggest you don't provide one, since the next time you use these key pair for login you need to input the passphrase although you won't need to enter the login password for that user.)   
    By default, `ras` key will be generated. It can be changed by specify `-t` argument to one of `rsa`, `dsa`, `ecdsa` or `ed25519`. This command will generate a key pair. In the public key, which ends with extension `.pub`, there is a comment following the ssh key in the end. The comment defaults to be `user@host`, which can be modified by providing `-C` argument.
2. To enable login without password for a user, first log in with that user account. Then in the home directory, create a `.ssh` folder and a file named `authorized_keys` inside that folder. Paste the content of your public key to the `authorized_keys` file. The trailing comment can be ignored.
3. By default, when you use `ssh` to login to a server without specifing the location of your ssh key, ssh keys in your `~/.ssh/` directory with name `id_rsa`, `id_dsa`, `id_ecdsa` or `id_ed25519` will searched to match the public key in the server. If you have changed the name or the location of your key, it will not be detected thus fail to login, in which case you will be prompted to input the password. What if you want to want to add another key to the search list? If you want to use a non-default file path for your key pair, you must configure your SSH client to find your private SSH key for connection to your server. For OpenSSH client on common operating system, the configuration is `~/.ssh/config`. Add following text to this file:
    ```
    # comment on which service this key is for
    Host <IP_or_HOST>
    PubkeyAuthentication yes
    IdentityFile <File_path_of_the_ssh_key>
    ```



### Is that reasonable to have multiple ssh key pairs?
Although it may seem easier to have only one key pair used for every site you want to login, have a unique key pair for each site will make it safer if one of these keys is compromised. Just put all key in the defalut `~/.ssh` directory and name it as you want to remind you each key is for what. Then configure them in the `~/.ssh/config` file.

