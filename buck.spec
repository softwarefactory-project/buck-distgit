Name:          buck
Version:       2016.11.11.01
Release:       1%{?dist}
Summary:       A fast build system that encourages the creation of small, reusable modules over a variety of platforms and languages.

License:       APACHE-2
URL:           https://buckbuild.com/
Source0:       https://github.com/facebook/buck/archive/79d36de9f5284f6e833cca81867d6088a25685fb.tar.gz
Source10:      buck.sh
Source11:      buckd.sh
BuildRequires: ant
BuildRequires: rsync
BuildRequires: gcc
Requires:      python
Requires:      java-devel

# TODO: make it works without this option
AutoReqProv:   no

%description
Buck is a build tool. To see what Buck can do for you, check out the documentation at http://buckbuild.com/.

%prep
%setup -q -n buck-79d36de9f5284f6e833cca81867d6088a25685fb

%build
ant
touch build/successful-build

%install
install -d -m 755 %{buildroot}%{_libexecdir}/buck

rsync -a programs/ %{buildroot}%{_libexecdir}/buck/programs/
rsync -a third-party/ %{buildroot}%{_libexecdir}/buck/third-party/
rsync -a build/ %{buildroot}%{_libexecdir}/buck/build/
rsync -a config/ %{buildroot}%{_libexecdir}/buck/config/

install -d -m 755 %{buildroot}%{_libexecdir}/buck/src/com/facebook/buck/python/

install -p -D -m 755 src/com/facebook/buck/python/pex.py %{buildroot}%{_libexecdir}/buck/src/com/facebook/buck/python/pex.py

# Fix permission error when trying to hard link pkg_resource from libexec
sed -i "s/hasattr(os, 'link'):/False:/" %{buildroot}%{_libexecdir}/buck/third-party/py/twitter-commons/src/python/twitter/common/python/common.py

install -p -D -m 755 %{SOURCE10} %{buildroot}%{_bindir}/buck
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_bindir}/buckd

%clean
# Remove ng.debug file
rm -Rf %{buildroot}/usr/lib/

%files
%{_libexecdir}/buck/
%{_bindir}/buck
%{_bindir}/buckd

%changelog
* Sun Dec 04 2016 Tristan Cacqueray <tdecacqu@redhat.com> 2016.11.11.01-1
- First (dirty) package
