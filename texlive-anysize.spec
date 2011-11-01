Name:		texlive-anysize
Version:	20090924
Release:	1
Summary:	A simple package to set up document margins
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anysize
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anysize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anysize.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package is considered obsolete; alternatives are the
typearea package from the koma-script bundle, or the geometry
package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/anysize/anysize.sty
%doc %{_texmfdistdir}/doc/latex/anysize/README
%doc %{_texmfdistdir}/doc/latex/anysize/anysize.pdf
%doc %{_texmfdistdir}/doc/latex/anysize/anysize.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
