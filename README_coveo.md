# Challenge

We want you to follow our regular [DevOps coding challenge](https://github.com/coveo/devops-coding-challenge). In order to
save your time, we provide you a basic Python implementation of the code to help you bootstrap the project.

You are free to simply use it and suggest some improvements you can see.

You can also just use it as a model and reimplement the required logic with the language of your choice. Please choose a
programming language you are comfortable with as we will certainly challenge you about your choices.

All steps listed below will be required during the interview. We expect you to do them BEFORE we meet.

- Make sure you can run the code and understand what's going on in the code.
- Review the code and take notes on stuff you would improve or change. Assume this code is in production right now and that
you have to plan the next few releases. Having an agile process in mind, what would you change in the first release, second
release, etc. This will help us focus our discussion on what's important first.
- Make sure to have a setup that allows you to hit a breakpoint and debug in a step-by-step manner. It doesn't matter which
application you use to do it, but make sure you're comfortable debugging in the environment you choose before the interview,
because bugs there will be 😉.
- Have an editor or IDE ready to code during the interview.
- Have Git installed.

We didn't follow our normal standards, so you should have something to say about that code.

We expect you to understand the whole project a minimum and have an opinion on it. We understand that you may not be 100%
familiar with AWS. It's normal and we don't expect you to learn everything before the interview.

## Running it

1. First you'll need to create an AWS account. One can be created for free.
2. Create an S3 bucket and upload some files into it. Bear in mind that there can be a charge if you go over the
[free tier requirements](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all&all-free-tier.q=S3&all-free-tier.q_operator=AND)
(5 GiB at time of writing).
3. To run the project itself, you'll need Python 3.8 or more recent and [Poetry](https://python-poetry.org/docs/#installation)
4. Run `poetry install`
5. Run `poetry run python ./main.py`

## During the technical interview

Be prepared for the pairs review during your technical interview. Also expect some additional challenges as we may ask you
to run your program in a different environment with a significant number of files.

## Final advice

Make sure you have fun while performing this challenge. It is very rare that candidates grasp the extent of the pitfalls to
avoid and all the technical challenges involved. We are not looking for perfection, but you will be evaluated on your ability
to adapt when we face the various problems that you will inevitably be confronted.

During the interview, treat the interviewers as colleagues. Feel free to ask for help as you would normally do in the course
of your job. They are there to help you, not to trick you. Their main objective is to find in you their future colleague with
whom they will enjoy working.

See you soon.
