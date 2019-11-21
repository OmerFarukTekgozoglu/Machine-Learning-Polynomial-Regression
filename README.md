# Machine-Learning-Polynomial-Regression

## What's the Polynomial Regression ? 

It's kind of a regression, be relax, we're still trying to find best fitting curve over our dataset. It's possible to finding a linear regression curve or finding a polynomial curve which fits better. Actually, it's depend on the how is the distribution your data. I mean you can easily test it with using basic matplotlib graphs. 

Poylnomial regression means that your are working exponential values, non linear maybe an logarithmic or simple equation like this;

``` y = ax + ax^2 + c ```

In the equation at the above y is the dependent variable, x is the independent variable, a is the coefficient, and c is a constant.

You can easily google it [GoogleIt](https://www.google.com.tr/search?client=opera&hs=V7v&sxsrf=ACYBGNSKF4vsYcztdkCtzg1AgRbzvkxSZQ%3A1574367384108&ei=mPDWXculBu6l1fAPxd2V0AU&q=what+is+the+polynomial+regression&oq=what+is+the+polynomial+regression&gs_l=psy-ab.3..0i22i30l10.239586.247216..247437...1.3..0.295.6679.0j17j16......0....1..gws-wiz.......0i71j35i39j0j0i131j35i39i19j0i67j0i131i67j0i203j0i22i10i30j0i19j0i22i30i19j0i13i30i19.O-Fgf1M1Oho&ved=0ahUKEwjL0bPFj_zlAhXuUhUIHcVuBVoQ4dUDCAo&uact=5)

## The Data
As you know, this codes comes from a video series on udemy.com but ı wrote every one of them carefully and I spent to much time to writing codes, playing with them, finding to hyper-parameters... 
So, I used basic data samples as same as the course's provides. In real world the data never goes like perfect fitting to a curve! But the this data perfectly fitting to x^3th degree curve. (1st area of the coordinate plate)

![Data](https://github.com/OmerFarukTekgozoglu/Machine-Learning-Polynomial-Regression/blob/master/Photos/DataSetScatterPlot.png?raw=True)

That's the data and we will find a curve to fits this data perfectly like this;

![Curve-1](https://github.com/OmerFarukTekgozoglu/Machine-Learning-Polynomial-Regression/blob/master/Photos/PolynomialRegressionResult.png?raw=True)

If you use the degree parameter 3;

![Curve-2](https://github.com/OmerFarukTekgozoglu/Machine-Learning-Polynomial-Regression/blob/master/Photos/PolynomialRegressionDegree3.png?raw=True)

Degree = 4;

![Curve-3](https://github.com/OmerFarukTekgozoglu/Machine-Learning-Polynomial-Regression/blob/master/Photos/PolynomialRegressionDegree4.png?raw=True)


What happens if you want to use linear regression;

![Curve-4](https://github.com/OmerFarukTekgozoglu/Machine-Learning-Polynomial-Regression/blob/master/Photos/linearRegressionResult.png?raw=True)


Ohh! It's bad isn't it? 

**Tricky Note**: If the data-set has outliers, don't use the polynomial regression, because polynomial regression can't handle with outliers and your prediction will be uncorrect. 
