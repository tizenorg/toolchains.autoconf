Name:           autoconf
Version:        2.68
Release:        1
License:        GPLv2+ and GFDL
Summary:        A GNU tool for automatically configuring source code
Url:            http://www.gnu.org/software/autoconf/
Group:          Development/Tools
Source:         http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.bz2
Source1:        filter-provides-automake.sh
Source2:        filter-requires-automake.sh
Source1001: packaging/autoconf.manifest 
BuildRequires:  m4 >= 1.4.7
Requires:       coreutils,
Requires:       grep
Requires:       m4 >= 1.4.7
BuildArch:      noarch

# filter out bogus perl(Autom4te*) dependencies
%define _use_internal_dependency_generator 0
%define __find_provides %{SOURCE1}
%define __find_requires %{SOURCE2}

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

You should install Autoconf if you are developing software and
would like to create shell scripts that configure your source code
packages. If you are installing Autoconf, you will also need to
install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
%setup -q
chmod +x %{SOURCE1}
chmod +x %{SOURCE2}

%build
cp %{SOURCE1001} .
# use ./configure here to avoid copying config.{sub,guess} with those from the
# rpm package
./configure --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
  --bindir=%{_bindir} --datadir=%{_datadir}
make #  %{?_smp_mflags}  Makefile not smp save

#check
#make check VERBOSE=yes

%install
%make_install

rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_datadir}/emacs

rm -rf %{buildroot}/%{_infodir}


%files
%manifest autoconf.manifest
%defattr(-,root,root,-)
%{_bindir}/*
# don't include standards.info, because it comes from binutils...
%{_datadir}/autoconf/*
%doc %{_mandir}/man1/*
%doc AUTHORS COPYING

