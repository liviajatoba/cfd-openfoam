reset

set terminal postscript eps enhanced color"Times-Roman" 18
set term png


set autoscale
set lmargin 13
set bmargin 4

#set output "Ux-linhaV.eps"
set output "Ux-linhaV.png"

set key center

set ylabel"{/*1.5{/Italic y(m)}" offset 1,0
set xlabel"{/*1.5{/Italic U_x (m/s)} }" offset 0,0


plot "../m01/postProcessing/sampleU/10/linhaV_U.xy"  using ($2):($1) title"{m01}" with lines lt 3 lw 2.5, \
     "../m02/postProcessing/sampleU/10/linhaV_U.xy"  using ($2):($1) title"{m02}" with lines lt 2 lw 2.5, \
     "../m03/postProcessing/sampleU/10/linhaV_U.xy"  using ($2):($1) title"{m03}" with lines lt 1 lw 2.5



