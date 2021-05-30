echo "-----------------------------------------"
sudo apt update
sudo apt upgrade -y
echo "-----------------------------------------"
echo "update and upgrade commands successful!"
echo "-----------------------------------------"
sudo apt install openssh-server -y
echo "-----------------------------------------"
echo "install openssh-server successful!"
echo "-----------------------------------------"
sudo apt install net-tools -y
echo "-----------------------------------------"
echo "install net-tools successful!"
echo "-----------------------------------------"
sudo apt install tree -y
echo "-----------------------------------------"
echo "install tree successful!"
echo "-----------------------------------------"
sudo apt install git -y
git config --global user.name "Markus Martin"
git config --global user.email "1986mmartin@gmail.com"
git config --global core.editor "vim"
git clone https://github.com/1986MMartin/coding-sections-markus $HOME/coding/coding-sections-markus
git clone https://github.com/1986MMartin/UdemyDataScience $HOME/coding/UdemyDataScience/
echo "-----------------------------------------"
echo "install git and set global config successful!"
echo "-----------------------------------------"
sudo apt install zsh -y
echo "-----------------------------------------"
echo "install zsh successful!"
echo "-----------------------------------------"
sudo apt install curl -y
echo "-----------------------------------------"
echo "install curl successful!"
echo "-----------------------------------------"
FOLDER=$HOME/Downloads
if [ -d "$FOLDER" ]; then
	echo "Folder $FOLDER exists."
else
	mkdir $FOLDER
fi
mkdir -p $HOME/Programme/vim/settings/vimundo
echo "-----------------------------------------"
echo "mkdir commands successful"
echo "-----------------------------------------"
cp -rf $HOME/coding/coding-sections-markus/linux_init/vim_settings/sample_vimrc.txt $HOME/.vimrc
echo "-----------------------------------------"
echo "vimrc successful!"
echo "-----------------------------------------"
sudo apt update
sudo apt upgrade -y
echo "-----------------------------------------"
echo "update and upgrade commands successful!"
echo "-----------------------------------------"
