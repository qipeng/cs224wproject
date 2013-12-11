warning('off','all');

% subplot(2,2,1);
% plotAlpha('ssredirect_ideg.txt');title('In degree, adaptive xmin');
% subplot(2,2,2);
% hold on;
% for xmin=10,
%     plotAlpha('ssredirect_ideg.txt',xmin);
% end
% title('In degree, fixed xmin (1-20)');
% 
% subplot(2,2,3);
% plotAlpha('ssredirect_odeg.txt');title('Out degree, adaptive xmin');
% subplot(2,2,4);
% hold on;
% for xmin=20,
%     plotAlpha('ssredirect_odeg.txt',xmin);
% end
plotAlpha('ssredirect_ideg.txt',10);
title('In degree, fixed xmin (10)');
plotAlpha('ssredirect_odeg.txt',20);
title('Out degree, fixed xmin (20)');