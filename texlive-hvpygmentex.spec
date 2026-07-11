%global tl_name hvpygmentex
%global tl_revision 62405

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Syntax-Highlighting of program code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hvpygmentex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvpygmentex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvpygmentex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is based on pygmentex but provides an automatic run from
within the document itself, with the option --shell-escape. It does not
need the additional action by the user to run the external program
pygmentize to create the code snippets.

