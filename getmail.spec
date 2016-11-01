Summary:	getmail - a mail retriever designed to allow you to get your mail
Summary(pl.UTF-8):	getmail - program do ściągania poczty
Name:		getmail
Version:	4.52.0
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
# Source0-md5:	5aa4dc9901bf4beb83ced9ac4bceaa9e
URL:		http://pyropus.ca/software/getmail/
BuildRequires:	python-devel >= 1:2.3.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
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

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install --prefix=%{_prefix} --install-purelib=%{py_sitescriptdir} --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{BUGS,CHANGELOG,THANKS,TODO,getmailrc-examples} docs/*.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/getmail*
%{_mandir}/man1/*
