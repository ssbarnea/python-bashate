# Created by pyp2rpm-3.2.1
%global pypi_name bashate

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        A pep8 equivalent for bash scripts

License:        TODO
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-pbr >= 1.8
BuildRequires:  python-hacking >= 0.10.0
BuildRequires:  python-hacking < 0.11
BuildRequires:  python-mock >= 1.2
BuildRequires:  python-coverage >= 3.6
BuildRequires:  python-discover
BuildRequires:  python-fixtures >= 1.3.1
BuildRequires:  python-subunit >= 0.0.18
BuildConflicts: python-sphinx = 1.3b1
BuildConflicts: python-sphinx = 1.2.0
BuildRequires:  python-sphinx >= 1.1.2
BuildRequires:  python-sphinx < 1.3
BuildRequires:  python-oslo-sphinx >= 2.5.0
BuildConflicts: python-oslo-sphinx = 3.4.0
BuildRequires:  python-testrepository >= 0.0.18
BuildRequires:  python-testscenarios >= 0.4
BuildRequires:  python-testtools >= 1.4.0
BuildRequires:  python-reno >= 0.1.1
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

%description
A pep8 equivalent for bash scriptsThis program attempts to be an automated
style checker for bash scripts to fill the same part of code review that pep8
does in most OpenStack projects. It started from humble beginnings in the
DevStack project, and will continue to evolve over time. Free software: Apache
license Documentation: Source: Bugs: Supported Checks Errors Basic white space
errors, for ...

%package -n     python2-%{pypi_name}
Summary:        A pep8 equivalent for bash scripts
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-pbr >= 1.6
Requires:       python-babel >= 1.3
Requires:       python-setuptools
%description -n python2-%{pypi_name}
A pep8 equivalent for bash scriptsThis program attempts to be an automated
style checker for bash scripts to fill the same part of code review that pep8
does in most OpenStack projects. It started from humble beginnings in the
DevStack project, and will continue to evolve over time. Free software: Apache
license Documentation: Source: Bugs: Supported Checks Errors Basic white space
errors, for ...

%package -n python-%{pypi_name}-doc
Summary:        bashate documentation
%description -n python-%{pypi_name}-doc
Documentation for bashate

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install
cp %{buildroot}/%{_bindir}/bashate %{buildroot}/%{_bindir}/bashate-2
ln -sf %{_bindir}/bashate-2 %{buildroot}/%{_bindir}/bashate-%{python2_version}


%check
%{__python2} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc doc/source/readme.rst README.rst
%{_bindir}/bashate
%{_bindir}/bashate-2
%{_bindir}/bashate-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Apr 25 2017 root - 0.5.1-1
- Initial package.