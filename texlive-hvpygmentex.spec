Name:		texlive-hvpygmentex
Version:	62405
Release:	2
Summary:	Syntax-Highlighting of program code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hvpygmentex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvpygmentex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvpygmentex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is based on pygmentex but provides an automatic run
from within the document itself, with the option
--shell-escape. It does not need the additional action by the
user to run the external program pygmentize to create the code
snippets.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hvpygmentex
%doc %{_texmfdistdir}/doc/latex/hvpygmentex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
