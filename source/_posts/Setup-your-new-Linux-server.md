---
title: Setup your new Linux server
date: 2017-12-27 11:07:21
tags:
categories: 
    - [UNIX, Basics]
---

### Create a new account 
After logging into your server as root through `ssh`, you neeed to create a new account for your development. For security, we should forbid login through root account.
1. Firstly, make sure you are logged in as root. If not, type `su - ` and enter the password for root;
2. `adduser <username>`, then type a password for this account;
3. To grant the user sudo priviliges, `usermod -aG sudo <username>`;
4. Now you can switch to that account by `su - <username>` and do some test, such as check you uid and groupid `id <username>`;
5. You can also check all existing account on your computer: `cat /etc/passwd` or `getent passwd`.

NOTE: By default on enterprise GNU/Linux and its derivatives, the `adduser` command creates a user which is disabled until you explicitly specify a password for that user. In this case, you need to set a password for that user with `passwd <username>`
