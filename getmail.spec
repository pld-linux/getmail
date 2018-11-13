Summary:	getmail - a mail retriever designed to allow you to get your mail
Summary(pl.UTF-8):	getmail - program do ściągania poczty
Name:		getmail
Version:	5.8
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
# Source0-md5:	99c02144d1238393fc1a7ff67964887d
URL:		http://pyropus.ca/software/getmail/
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
getmail is intended as a simple, secure, and reliable replacement for
fetchmail. It retrieves email (either all messages, or only unread
messages) from one or more POP3, SPDS, or IMAP4 servers (with or
without SSL) for one or more email accounts, and reliably delivers
into qmail-style Maildirs, mboxrd files, or through external MDAs
(command deliveries) specified on a per-account basis. getmail also
has excellent support for domain (multidrop) mailboxes, including
delivering messages to different users or destinations based on the
envelope recipient address.

%description -l pl.UTF-8
getmail ma być prostym, bezpiecznym i pewnym zamiennikiem fetchmaila.
Ściąga pocztę elektroniczną (wszystkie wiadomości albo tylko
nieprzeczytane) z jednego lub większej liczby serwerów POP3, SPDS lub
IMAP4 (z lub bez SSL) dla jednego lub większej liczby kont pocztowych,
a następnie w pewny sposób dostarcza ją do skrzynek Maildir w stylu
qmaila, plików mboxrd albo poprzez zewnętrzne polecenia MDA podawane
dla każdego konta. getmail ma także dobrą obsługę skrzynek domenowych
(multidrop), włącznie z dostarczaniem wiadomości do różnych
użytkowników lub celów w oparciu o adres adresata na kopercie.

%prep
%setup -q

# fix #!%{_bindir}/env python -> #!%{_bindir}/python:
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' %{name} %{name}-gmail-xoauth-tokens %{name}_{maildir,fetch,mbox} %{name}core/*.py

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*
%attr(755,root,root) %{_bindir}/getmail
%attr(755,root,root) %{_bindir}/getmail_fetch
%attr(755,root,root) %{_bindir}/getmail_maildir
%attr(755,root,root) %{_bindir}/getmail_mbox
%attr(755,root,root) %{_bindir}/getmail-gmail-xoauth-tokens
%{_mandir}/man1/getmail.1*
%{_mandir}/man1/getmail_fetch.1*
%{_mandir}/man1/getmail_maildir.1*
%{_mandir}/man1/getmail_mbox.1*
%{py_sitescriptdir}/getmail*.egg-info
%{py_sitescriptdir}/getmailcore/

