clear all

%% Read the file
fid = fopen('coins.dat');
M = str2double(fgetl(fid));     % number of types of coins
K = str2double(fgetl(fid    ));     % number of coins allowed
coins = strsplit(fgetl(fid), ' ');
s = zeros(1, M);                % types of coins
for m = 1:M
    s(m) = str2double(coins{m});
end
fclose(fid);
% M = 3; K = 5; s = [1 2 5];

%% DP - initialization
value = 1;
if min(s) == 1
    f(1) = 1;
else
    f(1) = K + 1;
end

%% DP - propogation [ I wish matlab is zero-indexed :( ]
while (f(value) <= K)
    value = value + 1;
    min_num = K + 1;
    for j = 1:length(s)
        if (value - s(j) > 0)
            min_num = min(min_num, f(value-s(j))+1);
        elseif (value - s(j) == 0)
            min_num = min(min_num, 1);
        end
    end
    f(value) = min_num;
end

%% output 
fprintf('Using at most %d coins, from the following values:\n  ', K);
for m = 1:M-1
    fprintf('%d, ', s(m));
end
fprintf('%d\n', s(M));
fprintf('The smallest value that can not be created is %d.\n', value);