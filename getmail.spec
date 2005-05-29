Summary:	getmail is a mail retriever designed to allow you to get your mail
Name:		getmail
Version:	4.3.10
Release:	0.1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
# Source0-md5:	98341b70159335e32eeb41d6cbd61e54
URL:		http://pyropus.ca/software/getmail/
BuildRequires:	python
BuildRequires:	python-modules >= 2.3.3
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
