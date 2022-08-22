reset

set terminal postscript eps enhanced color"Times-Roman" 18
set autoscale
set lmargin 13
set bmargin 4

set output "Co.eps"

set ylabel"{/*1.5{/Italic Courant}" offset 1,0
set xlabel"{/*1.5{/Italic t(s)} }" offset 0,0

#set logscale y
#set format y "%.1e"

plot "logs/CourantMax_0"  using ($1):($2) title"{max}" with lines lt 1 lw 2.5


