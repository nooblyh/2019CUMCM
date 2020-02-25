function [part1_of_P0] = pofP0(c,process_velocity,entryperson_per_miniute,k)
%UNTITLED2 此处显示有关此函数的摘要
%   此处显示详细说明
part1_of_P0 =0;
for i=0:(c-1)
    part1_of_P0 = part1_of_P0+(entryperson_per_miniute^i /(factorial(i)*((k*process_velocity))^i));
end

