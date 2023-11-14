reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "erroUx.eps"
set output "erroUx.png"

set key left

set xlabel"{/*1.5{/Italic y(m)}" offset 1,0
set ylabel"{/*1.5{/Italic erro %} }" offset 0,0

#set logscale y
set key right
set ytic 2

V = 1
h = 0.1
a = V/h
f(x) = a*x


plot "postProcessing/sampleU/0.6/linhaA.xy"  using ($1):(abs($2-f($1))*100/abs(f($1))) title"{0.6s}" with lines lt 2 lw 2.5, \
     "postProcessing/sampleU/0.4/linhaA.xy"  using ($1):(abs($2-f($1))*100/abs(f($1))) title"{0.4s}" with lines lt 3 lw 2.5, \
     "postProcessing/sampleU/0.2/linhaA.xy"  using ($1):(abs($2-f($1))*100/abs(f($1))) title"{0.2s}" with lines lt 4 lw 2.5
