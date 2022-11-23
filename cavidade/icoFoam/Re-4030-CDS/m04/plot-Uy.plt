reset

set terminal postscript eps enhanced color"Times-Roman" 18
set autoscale
set lmargin 13
set bmargin 4

set output "Uy.eps"

set xlabel"{/*1.5{/Italic d(m)}" offset 1,0
set ylabel"{/*1.5{/Italic U_y (m/s)} }" offset 0,0


plot "postProcessing/sample/10/linhaA_U.xy"  using ($1):($3) title"{Linha A}" with lines lt 3 lw 2.5, \
     "postProcessing/sample/10/linhaB_U.xy"  using ($1):($3) title"{Linha B}" with lines lt 2 lw 2.5



