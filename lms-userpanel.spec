# TODO:
#	- better files structure

%define		_cvs	20060721

Summary:	LAN Managment System - Userpanel
Summary(pl.UTF-8):   System Zarządzania Siecią Lokalną - Panel Użytkownika
Name:		lms-userpanel
Version:	1.1
Release:	0.%{_cvs}.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	userpanel-%{version}-cvs-%{_cvs}.tar.bz2
# Source0-md5:	9ce39bdd265376d90685a88846513e32
URL:		http://userpanel.rulez.pl/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	lms >= 1.6.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_lmsdir		%{_datadir}/lms
%define		_lmsvar		/var/lib/lms

%description
Userpanel is automated virtual customer service, based on LMS and
using its core features. It enables customers (or it's intended to) to
do review their payments, change their personal details or computer
properties, modify subscriptions, submit problems, track their
requests on Helpdesk and print invoices. It means, it makes a closer
contact with their ISP.

%description -l pl.UTF-8
Userpanel jest opartą na szkielecie LMS (i ściśle z LMS
współpracującą) implementacją tzw. e-boku. Umożliwia (albo będzie
umożliwiał) klientom przeglądanie stanu swoich wpłat, zmianę swoich
danych osobowych, edycję właściwości swoich komputerów, zmianę taryf,
zgłaszanie błędów oraz awarii do Helpdesku, wydruk faktur oraz
formularza przelewu.

%prep
%setup -q -n userpanel

%install
rm -rf $RPM_BUILD_ROOT
 
install -d $RPM_BUILD_ROOT%{_lmsdir}/userpanel
install -d $RPM_BUILD_ROOT%{_lmsdir}/www/userpanel/modules
install -d $RPM_BUILD_ROOT%{_lmsvar}/userpanel/templates_c

cp -R {lib,modules,templates}		$RPM_BUILD_ROOT%{_lmsdir}/userpanel
cp -R {index.php,style}			$RPM_BUILD_ROOT%{_lmsdir}/www/userpanel
ln -s %{_lmsdir}/www/userpanel/style	$RPM_BUILD_ROOT%{_lmsdir}/userpanel
ln -s %{_lmsvar}/userpanel/templates_c	$RPM_BUILD_ROOT%{_lmsdir}/userpanel

for MODULE in $RPM_BUILD_ROOT%{_lmsdir}/userpanel/modules/*; do
    MODULE=$(basename $MODULE)
    mkdir $RPM_BUILD_ROOT%{_lmsdir}/www/userpanel/modules/$MODULE
    ln -s %{_lmsdir}/userpanel/modules/$MODULE/style 	\
	$RPM_BUILD_ROOT%{_lmsdir}/www/userpanel/modules/$MODULE
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,COPYING,COPYRIGHTS,ChangeLog,README.html,ToDo.txt}
%doc %lang(pl) doc/README_pl.html
%dir %{_lmsvar}/userpanel
%attr(770,root,http) %{_lmsvar}/userpanel/templates_c
%{_lmsdir}/www/userpanel
%{_lmsdir}/userpanel
