Name:		texlive-anysize
Version:	15878
Release:	1
Summary:	A simple package to set up document margins
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anysize
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anysize.r15878.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anysize.doc.r15878.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
