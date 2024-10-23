reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "U-iter.eps"
set output "U-iter.png"

set ylabel"{/*1.5{/Italic U}" offset 1,0
set xlabel"{/*1.5{/Italic iter} }" offset 0,0

set key at 500,0.04,2
#set logscale y
#set format y "%.1e"

plot "postProcessing/probes/0/U"  using ($1):($2) title "{U_x P0}" with lines lt 1 lw 2.5, \
     "postProcessing/probes/0/U"  using ($1):($3) title "{U_y P0}" with lines lt 2 lw 2.5, \
     "postProcessing/probes/0/U"  using ($1):($5) title "{U_x P1}" with lines lt 3 lw 2.5, \
     "postProcessing/probes/0/U"  using ($1):($6) title "{U_y P1}" with lines lt 4 lw 2.5, \
     "postProcessing/probes/0/U"  using ($1):($8) title "{U_x P2}" with lines lt 5 lw 2.5, \
     "postProcessing/probes/0/U"  using ($1):($9) title "{U_y P2}" with lines lt 6 lw 2.5
