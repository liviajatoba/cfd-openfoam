reset

set terminal postscript eps enhanced color"Times-Roman" 18
set autoscale
set lmargin 13
set bmargin 4

set output "Fd.eps"

set xlabel"{/*1.5{/Italic t(s)}" offset 1,0
set ylabel"{/*1.5{/Italic F_d (N)} }" offset 0,0

set xrange [10:200]
set key left


plot "postProcessing/force/0/forces.dat"  using ($1):($2+$5) title"{Fx}" with lines lt 3 lw 2.5


