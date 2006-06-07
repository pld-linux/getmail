Summary:	getmail - a mail retriever designed to allow you to get your mail
Summary(pl):	getmail - program do ¶ci±gania poczty
Name:		getmail
Version:	4.6.1
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
# Source0-md5:	da61f99a3313b113ed44ae36dc70cf0f
URL:		http://pyropus.ca/software/getmail/
BuildRequires:	python-devel >= 2.3.3
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

%description -l pl
getmail ma byæ prostym, bezpiecznym i pewnym zamiennikiem fetchmaila.
¦ci±ga pocztê elektroniczn± (wszystkie wiadomo¶ci albo tylko
nieprzeczytane) z jednego lub wiêkszej liczby serwerów POP3, SPDS lub
IMAP4 (z lub bez SSL) dla jednego lub wiêkszej liczby kont pocztowych,
a nastêpnie w pewny sposób dostarcza j± do skrzynek Maildir w stylu
qmaila, plików mboxrd albo poprzez zewnêtrzne polecenia MDA podawane
dla ka¿dego konta. getmail ma tak¿e dobr± obs³ugê skrzynek domenowych
(multidrop), w³±cznie z dostarczaniem wiadomo¶ci do ró¿nych
u¿ytkowników lub celów w oparciu o adres adresata na kopercie.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{CHANGELOG,THANKS,TODO,getmailrc-examples} docs/*.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/getmailcore
%{_mandir}/man1/*
