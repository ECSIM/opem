function [ result ] = vector_filter( inp )
% Replace py.NoneType items with NaN
if isa(inp,'py.NoneType') == 1 
    result = NaN;
else
    result = double(inp);

end

end

