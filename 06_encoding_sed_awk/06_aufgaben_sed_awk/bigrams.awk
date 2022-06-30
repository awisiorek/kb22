#!/usr/bin/awk -f

BEGIN {
    lambda = 1
    if (ARGC > 0) {
        lambda = ARGV[1]
        delete ARGV[1]
    }
    SUBSEP = " "
    pre = ""
}

!/^$/ {
    for (i = 1; i <= NF; i++) {
        if (pre == "") {
            pre = $i
        } else {
            bigrams[pre, $i]++
            pre = $i
        }
    }
}

END {
    N = 0
    V = 0
    for (b in bigrams) {
        V++
        N += bigrams[b]
    }
    # printf "N=%d V=%d lambda=%f\n", N, V, lambda
    for (b in bigrams) {
        p = (bigrams[b] + lambda) / (N + V)
        printf "%s %f\n", b, p
    }
}
