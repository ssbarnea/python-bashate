%global pypi_name bashate

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        A pep8 equivalent for bash scripts

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/bashate
Source0:        https://pypi.io/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.

%package -n python2-%{pypi_name}
Summary:        A pep8 equivalent for bash scripts
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-fixtures
BuildRequires:  python-mock

Requires:       python-setuptools
Requires:       python-pbr
Requires:       python-babel

%description -n python2-%{pypi_name}
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        A pep8 equivalent for bash scripts
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-six

Requires:       python3-setuptools
Requires:       python3-pbr
Requires:       python3-babel

 
%description -n python3-%{pypi_name}
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.
%endif


%package -n python-%{pypi_name}-doc
Summary: Documentation for bashate module

BuildRequires:  python-six
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-reno


%description -n python-%{pypi_name}-doc
Documentation for the bashate module

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -rf {test-,}requirements.txt

%build
%py2_build
# doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd
rm -fr doc/build/html/.buildinfo

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/%{pypi_name} %{buildroot}%{_bindir}/%{pypi_name}-%{python3_version}
ln -s ./%{pypi_name}-%{python3_version} %{buildroot}%{_bindir}/%{pypi_name}-3
%endif

%py2_install
mv %{buildroot}%{_bindir}/%{pypi_name} %{buildroot}%{_bindir}/%{pypi_name}-%{python2_version}
ln -s ./%{pypi_name}-%{python2_version} %{buildroot}%{_bindir}/%{pypi_name}-2

%if 0%{?with_python3}
ln -s ./%{pypi_name}-3 %{buildroot}%{_bindir}/%{pypi_name}
%else
ln -s ./%{pypi_name}-2 %{buildroot}%{_bindir}/%{pypi_name}
%endif

%check
%{__python2} setup.py test

%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%if !0%{?with_python3}
%{_bindir}/%{pypi_name}
%endif
%{_bindir}/%{pypi_name}-2
%{_bindir}/%{pypi_name}-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-3
%{_bindir}/%{pypi_name}-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%changelog
* Sat Jun 25 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.5.1-1
- Upstream 0.5.1
- Fix python3 support (RHBZ#1314529)
- Use pypi.io URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Chandan Kumar <chkumar246@gmail.com> - 0.3.2-1
- Bumped to version 0.3.2
- Added missing test dependencies

* Wed Sep 30 2015 Chandan Kumar <chkumar246@gmail.com> -0.3.1-2
- Added python2 and python3 subpackage

* Wed Aug 12 2015 chandankumar <chkumar246@gmail.com> - 0.3.1-1
- Initial package.
