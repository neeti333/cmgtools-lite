#!/bin/bash

# for i in $(ls ./76X/);do
#     a=\"76X/$i\"
#     #    a=\"76X/WJetsToLNu\"
#     b=\"$i\"
#     root -l <<EOF
# .L selections.cxx+
# Selections s($a, $b);
# s.skimming();
# .q
# EOF
    
# done

a=\"76X/WJetsToLNu\"
b=\"WJetsToLNu\"
root -l <<EOF
    .L selections.cxx+
    Selections s($a, $b);
    s.skimming();
    .q
    EOF
EOF