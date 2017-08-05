#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mpich
Version  : 3.2
Release  : 22
URL      : http://www.mpich.org/static/downloads/3.2/mpich-3.2.tar.gz
Source0  : http://www.mpich.org/static/downloads/3.2/mpich-3.2.tar.gz
Summary  : High Performance and portable MPI
Group    : Development/Tools
License  : BSD-3-Clause mpich2
Requires: mpich-bin
Requires: mpich-lib
Requires: mpich-doc
BuildRequires : beignet-dev
BuildRequires : doxygen
BuildRequires : hwloc-dev
BuildRequires : libaio-dev
BuildRequires : libxml2-dev
BuildRequires : numactl-dev
BuildRequires : ocl-icd-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : psmisc
BuildRequires : python3-dev
BuildRequires : systemd-dev
BuildRequires : util-linux-dev
BuildRequires : valgrind-dev

%description
MPICH Release 3.2
MPICH is a high-performance and widely portable implementation of the
MPI-3.0 standard from the Argonne National Laboratory.  This release
has all MPI 3.0 functions and features required by the standard with
the exception of support for the "external32" portable I/O format and
user-defined data representations for I/O.

%package bin
Summary: bin components for the mpich package.
Group: Binaries

%description bin
bin components for the mpich package.


%package dev
Summary: dev components for the mpich package.
Group: Development
Requires: mpich-lib
Requires: mpich-bin
Provides: mpich-devel

%description dev
dev components for the mpich package.


%package doc
Summary: doc components for the mpich package.
Group: Documentation

%description doc
doc components for the mpich package.


%package lib
Summary: lib components for the mpich package.
Group: Libraries

%description lib
lib components for the mpich package.


%prep
%setup -q -n mpich-3.2
pushd ..
cp -a mpich-3.2 mpich-avx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501299209
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4-fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
%configure --disable-static --enable-fast=O3 --enable-yield=usleep --enable-handle-allocation=tls
make V=1  %{?_smp_mflags}

pushd ../mpich-avx2
export CFLAGS="$CFLAGS -march=haswell "
export FCFLAGS="$CFLAGS -march=haswell "
export FFLAGS="$CFLAGS -march=haswell "
export CXXFLAGS="$CXXFLAGS -march=haswell "
%configure --disable-static --enable-fast=O3 --enable-yield=usleep --enable-handle-allocation=tls --libdir=/usr/lib64/haswell
make V=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1501299209
rm -rf %{buildroot}
pushd ../mpich-avx2
%make_install
rm -rf %{buildroot}/usr/bin
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hydra_nameserver
/usr/bin/hydra_persist
/usr/bin/hydra_pmi_proxy
/usr/bin/mpic++
/usr/bin/mpicc
/usr/bin/mpichversion
/usr/bin/mpicxx
/usr/bin/mpiexec
/usr/bin/mpiexec.hydra
/usr/bin/mpif77
/usr/bin/mpif90
/usr/bin/mpifort
/usr/bin/mpirun
/usr/bin/mpivars
/usr/bin/parkill

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/mpi.mod
/usr/include/mpi_base.mod
/usr/include/mpi_constants.mod
/usr/include/mpi_sizeofs.mod
/usr/include/primitives/opa_by_lock.h
/usr/include/primitives/opa_emulated.h
/usr/include/primitives/opa_gcc_ia64.h
/usr/include/primitives/opa_gcc_intel_32_64.h
/usr/include/primitives/opa_gcc_intel_32_64_barrier.h
/usr/include/primitives/opa_gcc_intel_32_64_ops.h
/usr/include/primitives/opa_gcc_intel_32_64_p3.h
/usr/include/primitives/opa_gcc_intel_32_64_p3barrier.h
/usr/include/primitives/opa_gcc_intrinsics.h
/usr/include/primitives/opa_gcc_ppc.h
/usr/include/primitives/opa_gcc_sicortex.h
/usr/include/primitives/opa_nt_intrinsics.h
/usr/include/primitives/opa_sun_atomic_ops.h
/usr/include/primitives/opa_unsafe.h
/usr/lib64/libfmpich.so
/usr/lib64/libmpi.so
/usr/lib64/libmpich.so
/usr/lib64/libmpichcxx.so
/usr/lib64/libmpichf90.so
/usr/lib64/libmpicxx.so
/usr/lib64/libmpifort.so
/usr/lib64/libmpl.so
/usr/lib64/libopa.so
/usr/lib64/pkgconfig/mpich.pc
/usr/lib64/pkgconfig/openpa.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/mpich/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpi.so.12
/usr/lib64/libmpi.so.12.1.0
/usr/lib64/libmpicxx.so.12
/usr/lib64/libmpicxx.so.12.1.0
/usr/lib64/libmpifort.so.12
/usr/lib64/libmpifort.so.12.1.0
/usr/lib64/haswell/
