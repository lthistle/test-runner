
CXX=g++
CXX_FLAGS=-pthread -g -O0 -Wall -Werror -std=c++17

CXX_FILES=${wildcard *.cc}

TESTS=${subst .cc,.test,${CXX_FILES}}
PROGS=${subst .cc,.exe,${CXX_FILES}}
OK_FILES=${subst .cc,.ok,${CXX_FILES}}
OUT_FILES=${subst .cc,.out,${CXX_FILES}}
DIFF_FILES=${subst .cc,.diff,${CXX_FILES}}

all : Makefile ${PROGS};

test : Makefile ${TESTS}

${PROGS} : %.exe : Makefile %.cc ${wildcard src/*.cc} ${wildcard src/*.h}
	g++ -o $@ -I . -I src ${CXX_FLAGS} $*.cc ${wildcard src/*.cc}

${TESTS}: %.test : %.exe Makefile
	-./$*.exe  > $*.raw || true
	-@echo "no diff" > $*.diff
	-grep '^\*\*\*' $*.raw > $*.out || true
	-(diff $*.out $*.ok || true) > $*.diff 2>&1 || true
	-@echo "unknown" > $*.result
	-(((test -s $*.diff && echo "fail") || echo "pass") > $*.result) || true
	-@echo "$* ... $$(cat $*.result)"

clean:
	rm -rf *.exe *.diff *.out *.raw *.result
