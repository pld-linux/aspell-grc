Summary:	Ancient Greek dictionary for aspell
Summary(pl.UTF-8):	Słownik grecki starożytny dla aspella
Name:		aspell-grc
Version:	0.02
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/grc/aspell6-grc-%{version}-%{subv}.tar.bz2
# Source0-md5:	9a4ecc08569e4de53d35f16d1da02099
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ancient Greek dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik grecki starożytny (lista słów) dla aspella.

%prep
%setup -q -n aspell6-grc-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/grc.*
%{_datadir}/aspell/grc.dat
%{_datadir}/aspell/l-grc.*
