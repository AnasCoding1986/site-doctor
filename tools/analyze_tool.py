from bs4 import BeautifulSoup

def analyze_page(html: str) -> list[dict]:
    """
    Analyze HTML for accessibility and SEO violations.
    
    Returns list of violations with structure:
    {
        'type': violation type (str),
        'severity': 'high' | 'medium' | 'low',
        'element': HTML snippet (str),
        'suggestion': how to fix (str),
        'auto_fixable': bool
    }
    """
    violations = []
    
    try:
        soup = BeautifulSoup(html, 'html.parser')
    except Exception as e:
        return [{'type': 'parse_error', 'severity': 'high', 'element': '', 'suggestion': str(e), 'auto_fixable': False}]
    
    # 1. Missing alt text on images
    for img in soup.find_all('img'):
        if not img.get('alt') or img.get('alt').strip() == '':
            violations.append({
                'type': 'missing_alt_text',
                'severity': 'high',
                'element': str(img),
                'suggestion': 'Add descriptive alt text to image',
                'auto_fixable': True
            })
    
    # 2. Missing or empty <h1>
    h1_tags = soup.find_all('h1')
    if len(h1_tags) == 0:
        violations.append({
            'type': 'missing_h1',
            'severity': 'high',
            'element': '<h1> (missing)</h1>',
            'suggestion': 'Add an <h1> tag with main page title',
            'auto_fixable': True
        })
    elif any(not tag.get_text(strip=True) for tag in h1_tags):
        violations.append({
            'type': 'empty_h1',
            'severity': 'high',
            'element': '<h1></h1>',
            'suggestion': 'Fill <h1> with descriptive text',
            'auto_fixable': True
        })
    
    # 3. Missing meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if not meta_desc:
        violations.append({
            'type': 'missing_meta_description',
            'severity': 'medium',
            'element': '<meta name="description" (missing)>',
            'suggestion': 'Add meta description tag',
            'auto_fixable': True
        })
    
    # 4. Broken or empty anchor text
    for a in soup.find_all('a'):
        text = a.get_text(strip=True)
        if not text or text.lower() == 'click here':
            violations.append({
                'type': 'poor_anchor_text',
                'severity': 'medium',
                'element': str(a),
                'suggestion': 'Use descriptive anchor text',
                'auto_fixable': True
            })
    
    # 5. Missing lang attribute on <html>
    html_tag = soup.find('html')
    if not html_tag or not html_tag.get('lang'):
        violations.append({
            'type': 'missing_lang_attribute',
            'severity': 'medium',
            'element': '<html>',
            'suggestion': 'Add lang="en" to <html> tag',
            'auto_fixable': True
        })
    
    # 6. Contrast issues (flag only — cannot auto-fix)
    # Simple heuristic: check for light text on light backgrounds
    style_tags = soup.find_all('style')
    for style in style_tags:
        if 'color' in style.string.lower():
            violations.append({
                'type': 'potential_contrast_issue',
                'severity': 'low',
                'element': '<style>...</style>',
                'suggestion': 'Review color contrast ratios manually',
                'auto_fixable': False
            })
            break  # Only flag once
    
    return violations if violations else [{'type': 'no_issues', 'severity': 'info', 'element': '', 'suggestion': 'Page appears accessible', 'auto_fixable': False}]