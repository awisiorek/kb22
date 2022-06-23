#!/usr/bin/awk -f
{
    for (i = 1; i <= NF; i++) {
        mat[NR, i] = $i
    }
}

NF > max {
    max = NF
}

END {
    for (j = 1; j <= max; j++) {
        pre = ""
        for (i = 1; i <= NR; i++) {
            printf "%s%d", pre, mat[i, j]
            pre = " "
        }
        printf "\n"
    }
}