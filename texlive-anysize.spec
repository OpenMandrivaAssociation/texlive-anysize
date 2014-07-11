# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/anysize
# catalog-date 2009-09-24 14:57:17 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-anysize
Version:	20090924
Release:	8
Summary:	A simple package to set up document margins
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anysize
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anysize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anysize.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is considered obsolete; alternatives are the
typearea package from the koma-script bundle, or the geometry
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090924-2
+ Revision: 749281
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090924-1
+ Revision: 717838
- texlive-anysize
- texlive-anysize
- texlive-anysize
- texlive-anysize
- texlive-anysize

