function [ lab ] = rgb2lab( rgb )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    cform = makecform('srgb2lab');
    lab = applycform(rgb,cform);
end

