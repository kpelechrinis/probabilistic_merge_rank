<B>Problem</B>
Given a set of $m$ ``raters``, each of whom provides a ranking $R_i(n)$ of $n$ items, enumerated from $0$ to $n-1$, we want to provide a merged ranking $R_m(n)$ that maximizes the likelihood of observing these individual rankings by the raters. 

To solve this we will transform it to a problem of ranking through pairwise comparisons. More specifically we will sample each of the raters' rankings and generate pairwise comparisons of items uniformly at random. The sampling includes 2 steps: 

<ol>
  <li>Select uniformly at random one of the available raters</li>
  <li>Select uniformly at random two of the items and generate their relationship according to the sampled rater's ranking</li>
</ol>

This will provide us with $n_{sim}$ number of pairs $i \succ j$, with $i, j \in \{0, 1, ...,n-1\}$. These sampled pairs can now be considered as observations from a single ranking, i.e., the merged ranking we are looking for. With $p_i$ being the ``power rank`` of item $i$ in the merged rank, we can obtain these parameters by maximizing the likelihood of the observed (sampled) pairs: $\prod_{ij} \Pr[i \succ j]^{w_{ij}}$, where $w_{ij}$ is the number of times we have item $i$ being better than item $j$ in the observations and $\Pr[i \succ j] = \dfrac{p_i}{p_i+p_j}$, with $p_i \in \mathbb{R}^+$.

The ``pmr`` function implements the sampling and takes as input the number of simulations to perform and a dictionary, where each element is the list of each rater. Items need to be enumerated from 0, ..., $n$-1, while the raters are enumerated from 1, ... , $m$. 
