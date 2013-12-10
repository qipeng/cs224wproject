warning('off','all');

subplot(2,2,1);
plotAlpha('ssredirect_ideg.txt');title('In degree, adaptive xmin');
subplot(2,2,2);
hold on;
for xmin=1:20,
    plotAlpha('ssredirect_ideg.txt',xmin);
end
title('In degree, fixed xmin (1-20)');

subplot(2,2,3);
plotAlpha('ssredirect_odeg.txt');title('Out degree, adaptive xmin');
subplot(2,2,4);
hold on;
for xmin=1:20,
    plotAlpha('ssredirect_odeg.txt',xmin);
end
title('Out degree, fixed xmin (1-20)');