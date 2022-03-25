#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Unicodedata backport/updates to Python 3.x
Summary(pl.UTF-8):	Uaktualnienia danych Unicode dla Pythona 3.x
Name:		python3-unicodedata2
Version:	14.0.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/unicodedata2/
Source0:	https://files.pythonhosted.org/packages/source/u/unicodedata2/unicodedata2-%{version}.tar.gz
# Source0-md5:	06d009c4cc288fffeef3ecfb583197c5
URL:		https://pypi.org/project/unicodedata2/
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-libs >= 1:3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicodedata backport/updates to Python 3.x.

%description -l pl.UTF-8
Uaktualnienia danych Unicode dla Pythona 3.x.

%prep
%setup -q -n unicodedata2-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} tests/test_unicodedata2.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{py3_sitedir}/unicodedata2.cpython-*.so
%{py3_sitedir}/unicodedata2-%{version}-py*.egg-info
