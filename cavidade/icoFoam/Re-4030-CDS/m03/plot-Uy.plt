reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "Uy.eps"
set output "Uy.png"

set xlabel"{/*1.5{/Italic x(m)}" offset 1,0
set ylabel"{/*1.5{/Italic U_y (m/s)} }" offset 0,0


plot "postProcessing/sampleU/10/linhaH_U.xy" using ($1):($3) notitle"{Linha Horizontal}" with lines lt 3 lw 2.5



