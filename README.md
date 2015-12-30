###Dumps stylesheets from stylish extension for easy editing and version control.

*stylish-dump* was created by [spectralsun](https://github.com/spectralsun/stylish-dump), this repo is a fork.

##Install for Arch Linux

**Note:** The PKGBUILD will try to set up *stylish-dump*'s config file (`config.py`) for you (see details about `<user>` and `<profile>` below). 
Check the `PGKBUILD` before running `makepkg` **AND/OR** check out the `config.py` in `/opt/stylish-dump` after installed the package with pacman.

1. Download/save this with the name [PKGBUILD](https://raw.githubusercontent.com/spcmd/Scripts/master/PKGBUILDs/stylish-dump.PKGBUILD)
2. Put it somewhere (to an empty directory) and change to that directory, then run: `makepkg`. If it complains about missing dependencies, then run `makepkg -s` and it will install these dependencies for it: 
 * python2
 * python2-argh
 * python2-pathtools
 * python2-yaml
 * python2-sqlalchemy
 * python2-watchdog

Then you'll have the arch-package named: `stylish-dump-<version>-any.pkg.tar.xz`

Now you can install it with pacman's `-U` option:

`sudo pacman -U stylish-dump-<version>-any.pkg.tar.xz`


##Install manually:

**Note:** This install method (using /opt) is based on the PKGBUILD I've created for Arch Linux. You can set it up in another way (e.g.: put in under $HOME), but then you need to run the `python2 /path/to/stylish.py` directly **or** you need to edit the `stylish-dump` shell script to point to the proper directory (instead of /opt).

##### Make sure you have these dependencies installed:

* python2
* argh==0.26.1
* pathtools==0.1.2
* PyYAML==3.11
* SQLAlchemy==0.9.8
* watchdog==0.8.3

##### 1. Clone this repo: 

`git clone https://github.com/spcmd/stylish-dump.git`

##### 2. Edit `config.py` and change the `<user>` and `<profile>` strings to the proper ones (your username and the Firefox profile folder's name)

`DATABASE_URL = 'sqlite:////home/<user>/.mozilla/firefox/<profile>/stylish.sqlite'`

`OUTPUT_DIR = '/home/<user>/.stylish-dump'`

You can change the output directory where the .css files will be dumped. By default it's `~/.stylish-dump`, see: `OUTPUT_DIR` above.


##### 3. Put the needed files under /opt: 

`sudo mkdir -p /opt/stylish-dump`

`cp {config,database,stylish}.py /opt/stylish-dump`

##### 4. Put `stylish-dump` script to somewhere in your $PATH

but before make sure it's executable. If not, run:

`chmod +x stylish-dump`

Then copy somewhere (in your $PATH):

`cp stylish-dump /path/to/dir`


## Usage:

Simply run the `stylish-dump` command. By default it will dump the .css files to `~/.stylish-dump` directory (but you can change this directory, see: the second step of the **Install** above). After this, you can easily version control them with git.

stylish-dump runs in the foreground and keeps watching for modifications on the dumped .css files. You can exit it by pressing `^C` *(Ctrl+C)*.

Now you can edit the dumped .css file directly with you favorite editor (e.g.: vim), and stylish-dump will write back the changes to the Stylish addon's SQL database. However, in your browser you need to disable and re-enable the modified userstyle to see the changes.

The `stylish-dump -h` or `stylish-dump --help` command will give you some basic information.

####Reloading userstyles with Vimperator

If you are using [Vimperator](https://addons.mozilla.org/en-US/firefox/addon/vimperator), you can use the [stylish.js](https://github.com/spcmd/dotfiles/blob/master/vimperator/.vimperator/plugin/stylish.js) plugin to toggle a userstyle:

`:stylish toggle`

Or you can make a shorter custom command in your `~/.vimperatorrc`

`command! ST -description="Toggle Stylish userstyle for this page" :stylish toggle`

Or make a quick reload key combo (double toggle):

`nmap st :stylish toggle<CR>:stylish toggle<CR>`

Then source it in the browser (:source) or restart Firefox.

Now you can hit `st` to quickly reload the userstyle.

####Create backup of the stylish.sqlite database

stylish-dump allows you to quickly create backup of the stylish.sqlite database with the following options:

`-b, --backup <dest_dir>` Create a backup of the Stylish SQLite database to <dest_dir>.

`-B, --quick-backup` Create a quick backup of the Stylish SQLite database in the same directory (by default it's the Firefox profile directory).

The backup copies will have date&time stamps in their filenames so they won't get overwritten, you can make as many backups as you wish.
