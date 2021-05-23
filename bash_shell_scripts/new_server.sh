echo "-----------------------------------------"
sudo apt-get update
sudo apt-get upgrade -y

echo "-----------------------------------------"
echo "update and upgrade commands successful!"
echo "-----------------------------------------"

sudo apt-get install openssh-server -y

echo "-----------------------------------------"
echo "install openssh-server successful!"
echo "-----------------------------------------"

sudo apt-get install net-tools -y

echo "-----------------------------------------"
echo "install net-tools successful!"
echo "-----------------------------------------"

sudo apt-get install tree -y

echo "-----------------------------------------"
echo "install tree successful!"
echo "-----------------------------------------"

sudo apt-get install git -y
git config --global user.name "Markus Martin"
git config --global user.email "1986mmartin@gmail.com"
git config --global core.editor "vim"
git clone https://github.com/1986MMartin/coding-sections-markus $HOME/coding/coding-sections-markus
git clone https://github.com/1986MMartin/UdemyDataScience $HOME/coding/UdemyDataScience/

echo "-----------------------------------------"
echo "install git and set global config successful!"
echo "-----------------------------------------"

sudo apt-get install zsh -y

echo "-----------------------------------------"
echo "install zsh successful!"
echo "-----------------------------------------"

# mkdir $HOME/coding
mkdir $HOME/Downloads
mkdir $HOME/Programme
mkdir $HOME/Programme/vim
mkdir $HOME/Programme/vim/settings
mkdir $HOME/Programme/vim/settings/vimundo

echo "-----------------------------------------"
echo "mkdir commands successful"
echo "-----------------------------------------"

sudo apt-get update
sudo apt-get upgrade -y

echo "-----------------------------------------"
echo "update and upgrade commands successful!"
echo "-----------------------------------------"
