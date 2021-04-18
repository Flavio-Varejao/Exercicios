#!/usr/bin/env bash
 
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a=80000; pop_b=200000; ano=0

while :; do
    pop_a=$(bc <<< "$pop_a * 1.03")
    pop_b=$(bc <<< "$pop_b * 1.015")
    let ano++
    (($(bc <<< "$pop_a>=$pop_b") > 0)) && break
done
echo "A ultrapassa B em $ano anos"  

#######################################################################################
# pop_a=80000
# pop_b=200000
# 
# while ((pop_a<pop_b))
# do
#     pop_a=$((pop_a * (1000+30)/1000))
#     pop_b=$((pop_b * (1000+15)/1000))
#     ((++ano))
# done
# echo "A ultrapassa B em $ano anos"
########################################################################################
# pop_a=80000
# pop_b=200000
# ano=0
# stt=0
# 
# while ((${stt} < 1)); do
#     pop_a=$(bc <<< "${pop_a} * 1.03")
#     pop_b=$(bc <<< "${pop_b} * 1.015")
#     let ano++
#     stt=$(bc <<< "${pop_a}>=${pop_b}")
# Linha Abaixo é para testes#
# printf "PAIS_A: %s =» PAIS_B: %s =» ANO: %02d  =» STT: %d\n" "${pop_a}" "${pop_b}" "${ano}" "${stt}"
# done
# echo -e "\nA população de A: ${pop_a} \">=\" A população de B:${pop_b} em $ano anos"
#######################################################################################
# awk '{ano=0;pa=80000;pb=200000;}
# {while(pa<pb){ano+=1;pa=(pa*1.03);pb=(pb*1.015);printf "PA: %s PB: %s Ano: %02d\n",pa,pb,ano}
# {print "\nPA superou PB em " ano" anos\n"}}' <<< ""  
