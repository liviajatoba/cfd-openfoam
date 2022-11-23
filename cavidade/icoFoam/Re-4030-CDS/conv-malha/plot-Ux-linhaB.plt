reset

set terminal postscript eps enhanced color"Times-Roman" 18
set autoscale
set lmargin 13
set bmargin 4

set output "Ux-linhaB.eps"

set xlabel"{/*1.5{/Italic d(m)}" offset 1,0
set ylabel"{/*1.5{/Italic U_y (m/s)} }" offset 0,0


plot "../m01/postProcessing/sample/10/linhaB_U.xy"  using ($1):($2) title"{m01}" with lines lt 3 lw 2.5, \
     "../m02/postProcessing/sample/10/linhaB_U.xy"  using ($1):($2) title"{m02}" with lines lt 2 lw 2.5, \
     "../m03/postProcessing/sample/10/linhaB_U.xy"  using ($1):($2) title"{m03}" with lines lt 1 lw 2.5, \
     "../m04/postProcessing/sample/10/linhaB_U.xy"  using ($1):($2) title"{m04}" with lines lt 4 lw 2.5


