%global tl_name context-legacy
%global tl_revision 79616

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The ConTeXt macro package, MkII
Group:		Publishing
URL:		https://www.ctan.org/pkg/context-legacy
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-legacy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-legacy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(amsfonts)
Requires:	texlive(context)
Requires:	texlive(context-legacy.bin)
Requires:	texlive(lm)
Requires:	texlive(ly1)
Requires:	texlive(manfnt-font)
Requires:	texlive(mflogo-font)
Requires:	texlive(mptopdf)
Requires:	texlive(pdftex)
Requires:	texlive(stmaryrd)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In TeX Live, ConTeXt MkII is split from current ConTeXt (MkIV and
newer). We use the ConTeXt repackaging as distributed from
https://github.com/gucci-on-fleek/context-packaging. See
https://contextgarden.net and https://pragma-ade.com for information
about ConTeXt.

