#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Allow to inject warning filters during nosetest
Summary(pl.UTF-8):	Możliwość wstrzyknięcia filtrów ostrzeżeń podczas nosetestów
Name:		python-nose_warnings_filters
Version:	0.1.5
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nose-warnings-filters/
Source0:	https://files.pythonhosted.org/packages/source/n/nose_warnings_filters/nose_warnings_filters-%{version}.tar.gz
# Source0-md5:	b66f5357d86e0494f0cbafa80c1239f4
URL:		https://pypi.org/project/nose_warnings_filters/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allow to inject warning filters during nosetest.

%description -l pl.UTF-8
Możliwość wstrzyknięcia filtrów ostrzeżeń podczas nosetestów.

%package -n python3-nose_warnings_filters
Summary:	Allow to inject warning filters during nosetest
Summary(pl.UTF-8):	Możliwość wstrzyknięcia filtrów ostrzeżeń podczas nosetestów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-nose_warnings_filters
Allow to inject warning filters during nosetest.

%description -n python3-nose_warnings_filters -l pl.UTF-8
Możliwość wstrzyknięcia filtrów ostrzeżeń podczas nosetestów.

%prep
%setup -q -n nose_warnings_filters-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
nosetests-%{py_ver} nose_warnings_filters/testing
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
nosetests-%{py3_ver} nose_warnings_filters/testing
%endif
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
%{py_sitescriptdir}/nose_warnings_filters
%{py_sitescriptdir}/nose_warnings_filters-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nose_warnings_filters
%defattr(644,root,root,755)
%{py3_sitescriptdir}/nose_warnings_filters
%{py3_sitescriptdir}/nose_warnings_filters-%{version}-py*.egg-info
%endif
