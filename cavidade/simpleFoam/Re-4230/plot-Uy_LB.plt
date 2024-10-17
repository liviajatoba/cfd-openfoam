reset

set terminal postscript eps enhanced color"Times-Roman" 18
set term png


set autoscale
set lmargin 13
set bmargin 4

set output "Fig7b-Uy-LB.png"

set key bottom left
set title "(b) U_y em x = 0,048 m"
set ylabel"{/*1.5{/Italic y(m)}" offset 1,0
set xlabel"{/*1.5{/Italic U_y (m/s) } }" offset 0,0
set yrange[-0.05:0]


plot "postProcessing/sampleU/2000/LB.xy"  using ($3):($1) title "{num}" with lines lt 1 lw 2.5, \
     "dados/LB_Uy_0.048m.dat"  using ($1):($2) title "{Ref.}" with lines lt 2 lw 2.5



