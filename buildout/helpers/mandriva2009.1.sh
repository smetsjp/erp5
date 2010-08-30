#!/bin/sh

USAGE="""\
Helper for buildout-base installation of ERP5 on Mandriva 2009.1.
 Usage:
   mandriva2009.1.sh [-h|-l]

   With no options, attempts to install the dependencies required
   to run the buildout.

 Options:
   -h  shows this message
   -l  lists the required dependencies\
"""
PACKAGE_LIST="""\
automake
bison
cpio
flex
gcc
gcc-c++
gettext
groff
libSDL-devel
libSDL_gfx-devel
libSDL_image-devel
libboost-devel
libbzip2-devel
libgdbm-devel
libglib2-devel
libgomp-devel
libjpeg-devel
libldap-devel
libncurses-devel
libneon0.27-devel
libopenssl-devel
libpng-devel
libreadline-devel
librsync-devel
libsasl2-devel
libtermcap-devel
libtiff3-devel
libtool
libungif-devel
libxml2-devel
libxslt-devel
make
patch
python-devel
python-setuptools
rpm
subversion
subversion-devel
subversion-tools
tesseract-devel
x11-server-xvfb
zip
zlib1-devel\
"""
if [ x"$1" == x ]; then
  urpmi $PACKAGE_LIST
elif [ "$1" = "-l" ]; then
  echo "$PACKAGE_LIST"
elif [ "$1" = "-h" ]; then
  echo "$USAGE"
else
  echo "Unknown argument."
  echo "$USAGE"
fi