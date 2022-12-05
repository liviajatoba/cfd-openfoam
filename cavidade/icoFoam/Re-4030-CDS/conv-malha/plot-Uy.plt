reset

set terminal postscript eps enhanced color"Times-Roman" 18
set term png


set autoscale
set lmargin 13
set bmargin 4

#set output "Uy-linhaH.eps"
set output "Uy-linhaH.png"


set xlabel"{/*1.5{/Italic x(m)}" offset 1,0
set ylabel"{/*1.5{/Italic U_y (m/s)} }" offset 0,0


plot "../m01/postProcessing/sampleU/10/linhaH_U.xy"  using ($1):($3) title"{m01}" with lines lt 3 lw 2.5, \
     "../m02/postProcessing/sampleU/10/linhaH_U.xy"  using ($1):($3) title"{m02}" with lines lt 2 lw 2.5, \
     "../m03/postProcessing/sampleU/10/linhaH_U.xy"  using ($1):($3) title"{m03}" with lines lt 1 lw 2.5


