function [ result ] = vector_filter( inp )
%vector_filter Summary of this function goes here
%   Detailed explanation goes here
if isa(inp,'py.NoneType') == 1 
    result = NaN;
else
    result = double(inp);

end

end

