function alphas=plotAlpha(filename,xminall)
    degs = load(filename);
    months = size(degs,1);
    alphas = zeros(months,1);
    
    for month=1:months,
        pdf = degs(month,2:end-1);
        if ~exist('xminall','var') || isempty(xminall),
            xmin = bestxmin(pdf);
        else
            xmin = xminall;
        end
        alpha = mlAlpha(pdf, xmin);
        alphas(month) = alpha;
    end
    
    plot(alphas);
end

function xmin = bestxmin(pdf)
    minval = inf;
    retxmin = 1;
    sumpdf = sum(pdf);
    for xm = 1:length(pdf),
        cdf = pdf(xm:end);
        for i = 2:length(cdf),
            cdf(i) = cdf(i) + cdf(i-1);
        end
        cdf = cdf(:);
        if (cdf(end)/sumpdf<.5),break;end
        x = pdf(xm:end);
        x = [x(:), ones(length(x),1)];
        theta = (x'*x)\(x'*cdf);
        val = max(abs(x*theta-cdf));
        if (val < minval),
            minval = val;
            retxmin = xm;
        end
    end
    xmin = double(retxmin);
%     fprintf('xmin=%f\n',xmin);
end

function alpha = mlAlpha(pdf, xmin)
    n = sum(pdf(ceil(xmin):end));
    a = 0;
    
    for i=ceil(xmin):length(pdf),
        a = a + pdf(i) * log(i / xmin);
    end
    
    alpha = n/a + 1;
end