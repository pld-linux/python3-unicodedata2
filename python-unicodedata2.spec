#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Unicodedata backport/updates to Python 2.x
Summary(pl.UTF-8):	Uaktualnienia danych Unicode dla Pythona 2.x
Name:		python-unicodedata2
Version:	12.1.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/unicodedata2/
Source0:	https://files.pythonhosted.org/packages/source/u/unicodedata2/unicodedata2-%{version}.tar.gz
# Source0-md5:	a4d781b0d59a8cb9243d4a84aa10fbd9
URL:		https://pypi.org/project/unicodedata2/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 2.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-libs >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicodedata backport/updates to Python 2.x.

Additionally this module backports named aliases and named sequences
support to Python 2.

%description -l pl.UTF-8
Uaktualnienia danych Unicode dla Pythona 2.x.

Dodatkowo ten moduł zawiera backport nazwanych aliasów i nazwanych
sekwencji do Pythona 2.

%package -n python3-unicodedata2
Summary:	Unicodedata backport/updates to Python 3.x
Summary(pl.UTF-8):	Uaktualnienia danych Unicode dla Pythona 3.x
Group:		Libraries/Python
Requires:	python3-libs >= 1:3.2

%description -n python3-unicodedata2
Unicodedata backport/updates to Python 3.x.

%description -n python3-unicodedata2 -l pl.UTF-8
Uaktualnienia danych Unicode dla Pythona 3.x.

%prep
%setup -q -n unicodedata2-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{py_sitedir}/unicodedata2.so
%{py_sitedir}/unicodedata2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-unicodedata2
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{py3_sitedir}/unicodedata2.cpython-*.so
%{py3_sitedir}/unicodedata2-%{version}-py*.egg-info
%endif
