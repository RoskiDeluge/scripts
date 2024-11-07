# How to Add Aliases for Scripts

This guide will help you create quick aliases for the scripts located in the `/Users/path/to/scripts` directory using Zsh on a MacOS system.

## Steps

1. **Open Terminal**

   First, open your Terminal application. You can find it in the Utilities folder under Applications or by using Spotlight (⌘ + Space) and typing "Terminal".

2. **Navigate to Scripts Directory**

   Use the `cd` command to change to your scripts directory:
   ```bash
   cd /Users/robertodelgado/scripts
   ```	

3. **Open `.zshrc` File**

   The `.zshrc` file is where you add your aliases. You can open it using a text editor of your choice. Here, we'll use `nano`:

   ```bash
   nano ~/.zshrc
   ```

4. **Add Aliases**

   Scroll to the end of the file and add your aliases. For example, if you have a script called `myscript.sh` in the `/Users/path/to/scripts` directory, you can add:

   ```bash
   alias myscript='~/scripts/myscript.sh'
   ```

5. **Save and Exit**

   Save and exit the editor. If you are using `nano`, you can do this by pressing `CTRL + X`, then `Y` to confirm changes and `Enter` to return to the command line.

6. **Apply Changes**

   Apply the new aliases by sourcing the `.zshrc` file:

   ```bash
      source ~/.zshrc
   ```

7. **Using Aliases**

   You can now use the alias you've created by simply typing `myscript` in the terminal:

   ```bash
   myscript
   ```
